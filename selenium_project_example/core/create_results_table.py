from selenium_project_example.core.infrastructure.models.test_result import \
    Base
from selenium_project_example.core.infrastructure.session import engine

Base.metadata.create_all(engine)
