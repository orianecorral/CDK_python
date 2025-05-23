from aws_cdk import Stack, Duration
from constructs import Construct
from aws_cdk import (
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_sqs as sqs,
)
from aws_cdk.aws_lambda_event_sources import SqsEventSource

class CdkPythonStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Création d'un bucket S3 (non utilisé ici mais pour test)
        s3.Bucket(self, "MyFirstBucket")

        # Création de la file SQS
        queue = sqs.Queue(
            self, "MyQueue",
            visibility_timeout=Duration.seconds(300),
        )

        # Fonction Lambda déclenchée par SQS
        sqs_lambda = _lambda.Function(
            self, "SqsLambda",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda_handler.handler",  # ← chemin vers ta fonction
            code=_lambda.Code.from_asset("lambda_handler"),  # ← dossier contenant ton .py
        )

        # Création du déclencheur depuis SQS
        sqs_event_source = SqsEventSource(queue)
        sqs_lambda.add_event_source(sqs_event_source)
