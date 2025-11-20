try:
    from datetime import datetime
    print("datetime import: SUCCESS")
except ImportError as e:
    print(f"datetime import: FAILED - {e}")

try:
    from src.utils.logger import WorkflowLogger
    print("WorkflowLogger import: SUCCESS")
except ImportError as e:
    print(f"WorkflowLogger import: FAILED - {e}")

try:
    from src.models.workflow import Workflow, Task
    print("Workflow/Task import: SUCCESS")
except ImportError as e:
    print(f"Workflow/Task import: FAILED - {e}")

try:
    logger = WorkflowLogger()
    logger.log_error("test", "test", "test error")
    print("Logger functionality: SUCCESS")
except Exception as e:
    print(f"Logger functionality: FAILED - {e}")