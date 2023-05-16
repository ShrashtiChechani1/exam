from django.conf.urls import include
from app.mark_attendance import mark_attendance
from app.leave import apply_leave
from app.leave import leave_history
from app.manager import approve_reject_leave
from django.urls import re_path as url


urlpatterns = [
     url('mark_attendance', mark_attendance, name="mark_attendance"),
     url('apply_leave',apply_leave,name="apply_leave"),
     url('leave_history',leave_history,name="leave_history"),
     url('approve_reject_leave',approve_reject_leave,name="approve_reject_leave")




]