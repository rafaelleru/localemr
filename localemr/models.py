from localemr.emr.models import EMRStepStates, FailureDetails


class SparkResult:
    def __init__(self, state: EMRStepStates, failure_details: FailureDetails):
        self.state = state
        self.failure_details = failure_details


class Configuration:
    def __init__(self, fetch_from_s3=False, convert_s3_to_local=True, local_dir=None, livy_host='http://livy:8998'):
        self.fetch_from_s3 = fetch_from_s3
        self.convert_s3_to_local = convert_s3_to_local
        # If local_dir not specified temporary directories will be used
        self.local_dir = local_dir
        self.livy_host = livy_host


CONF = Configuration()