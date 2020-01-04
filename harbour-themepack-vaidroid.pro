TEMPLATE = aux

NAME=harbour-themepack-vaidroid

OTHER_FILES = \
        theme/* \
        apk/192x192/* \
        overlay/* \
        rpm/* 

apk/192x192.files = apk/192x192/*
apk/192x192.path = /usr/share/harbour-themepack-vaidroid/apk/192x192/

overlay.files = overlay/*
overlay.path = /usr/share/harbour-themepack-vaidroid/overlay/

theme.files = theme/*
theme.path = /usr/share/harbour-themepack-vaidroid/theme/

INSTALLS += \
        theme \
        apk/192x192 \
        overlay

