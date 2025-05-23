def handler(event, context):
    """
    AWS Lambda function handler.
    :param event: The event data passed to the Lambda function.
    :param context: The context object provided by AWS Lambda.
    :return: A response indicating the function was invoked successfully.
    """
    print("Lambda function invoked with event:", event)
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }