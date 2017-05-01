from flask import Blueprint, current_app, request

from lightflow.workflows import start_workflow, stop_workflow
from lightflow.models.exceptions import (WorkflowArgumentError,
                                         WorkflowImportError)

from lightflow_rest.core.response import StatusCode, ApiResponse, ApiError


api = Blueprint('workflow', __name__, url_prefix='/workflow')


@api.route('/<name>', methods=['POST'])
def api_start_workflow(name):
    """ Endpoint for starting a new workflow.
    
    The dynamic path variable <name> is the name of the workflow that should be started.
    The endpoint accepts a parameter keep_data (e.g. ?keep_data=1) that tells the system
    to not delete the workflow data in the persistent storage. Arguments for the
    workflow are sent as form-encoded data. 
    """
    try:
        keep_data = request.args.get('keep_data', None)
        if keep_data is not None:
            if keep_data not in ['0', '1']:
                raise ApiError(StatusCode.BadRequest,
                               'The keep_data argument must be either 0 or 1.')
            else:
                keep_data = bool(int(keep_data))
        else:
            keep_data = False

        id = start_workflow(name=name,
                            config=current_app.config['LIGHTFLOW'],
                            clear_data_store=not keep_data,
                            store_args=request.form.to_dict())

        return ApiResponse({'id': id})
    except (WorkflowArgumentError, WorkflowImportError) as err:
        raise ApiError(StatusCode.InternalServerError, str(err))


@api.route('/', methods=['DELETE'])
@api.route('/<name>', methods=['DELETE'])
def api_stop_workflow(name=None):
    """ Endpoint for stopping all or a single running workflow.

    This endpoint can be called with either a dynamic path variable <name>, specifying
    the job that should be stopped, or without one which will stop all running workflows.
    """
    try:
        stop_workflow(current_app.config['LIGHTFLOW'],
                      names=[name] if name is not None else None)
        return ApiResponse({'success': True})
    except Exception as err:
        raise ApiError(StatusCode.InternalServerError, str(err))


@api.route('/', methods=['GET'])
def api_list_workflows(name):
    pass
