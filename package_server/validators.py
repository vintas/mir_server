import re
from django.core.exceptions import ValidationError

SEMVER_PATTERN = r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$'

def validate_semver(value):
    if not re.match(SEMVER_PATTERN, value):
        raise ValidationError(
            '%(value)s is not a valid semantic version (MAJOR.MINOR.PATCH)',
            params={'value': value},
        )
