from rest_framework.routers import DefaultRouter
from .views import EmployeeViewset, TaskViewset

router  = DefaultRouter()
router.register('employees', EmployeeViewset)
router.register('tasks', TaskViewset)

urlpatterns = router.urls