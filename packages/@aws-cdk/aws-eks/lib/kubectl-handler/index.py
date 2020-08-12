import json
import logging

from apply import apply_handler
from helm import helm_handler
from patch import patch_handler
from get import get_handler

def handler(event, context):
  print(json.dumps(event))

  resource_type = event['ResourceType']
  if resource_type == 'Custom::AWSCDK-EKS-KubernetesResource':
    return apply_handler(event, context)

  if resource_type == 'Custom::AWSCDK-EKS-HelmChart':
    return helm_handler(event, context)

  if resource_type == 'Custom::AWSCDK-EKS-KubernetesPatch':
    return patch_handler(event, context)

  if resource_type == 'Custom::AWSCDK-EKS-KubernetesResourceAttribute':
    return get_handler(event, context)

  raise Exception("unknown resource type %s" % resource_type)
