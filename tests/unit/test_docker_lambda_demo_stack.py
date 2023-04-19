import aws_cdk as core
import aws_cdk.assertions as assertions

from docker_lambda_demo.docker_lambda_demo_stack import DockerLambdaDemoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in docker_lambda_demo/docker_lambda_demo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DockerLambdaDemoStack(app, "docker-lambda-demo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
