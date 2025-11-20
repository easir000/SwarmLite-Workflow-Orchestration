import pytest
from src.orchestrator.parser import WorkflowParser
from src.models.workflow import Workflow, Task

def test_parse_workflow():
    parser = WorkflowParser()
    
    workflow_def = """
    workflow_id: test_workflow
    tasks:
      - id: task1
        type: python
        depends_on: []
      - id: task2
        type: http
        depends_on: [task1]
    retry_policy:
      max_attempts: 3
      delay_seconds: 2
    """
    
    workflow = parser.parse(workflow_def)
    
    assert workflow.id == "test_workflow"
    assert len(workflow.tasks) == 2
    assert workflow.tasks[0].id == "task1"
    assert workflow.tasks[1].id == "task2"
    assert workflow.retry_policy.max_attempts == 3

def test_validate_dag():
    parser = WorkflowParser()
    
    workflow_def = """
    workflow_id: test_dag
    tasks:
      - id: task1
        type: python
        depends_on: []
      - id: task2
        type: python
        depends_on: [task1]
      - id: task3
        type: python
        depends_on: [task2]
    """
    
    workflow = parser.parse(workflow_def)
    assert parser.validate_dag(workflow) == True

def test_circular_dependency():
    parser = WorkflowParser()
    
    workflow_def = """
    workflow_id: test_circular
    tasks:
      - id: task1
        type: python
        depends_on: [task2]
      - id: task2
        type: python
        depends_on: [task1]
    """
    
    workflow = parser.parse(workflow_def)
    with pytest.raises(ValueError, match="circular dependencies"):
        parser.validate_dag(workflow)