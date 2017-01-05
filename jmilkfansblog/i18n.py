import oslo_i18n as i18n

DOMAIN = 'jmilkfansblog'

_translatiors = i18n.TranslatorFactory(domain=DOMAIN)

# The primary translation function using the well-known name "_"
_ = _translatiors.primary

# Translators for log levels.
#
# The abbreviated names are meant to reflect the usual use of a short
# name like '_'. The "L" is for "log" and the other letter comes from
# the level.
_LI = _translatiors.log_info
_LW = _translatiors.log_warning
_LE = _translatiors.log_error
_LC = _translatiors.log_critical
