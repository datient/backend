from .doctor import DoctorViewSet
from .hospital import HospitalizationViewSet
from .infraestructure import BedViewSet, RoomViewSet
from .jwt import obtain_jwt_token
from .patient import (ComplementaryStudyViewSet, FuturePlanViewSet,
                       PatientViewSet, ProgressViewSet)
from .pdf import generate_pdf
from .statistics import generate_statistics
