#include <QtGlobal>

extern "C" {
    const char* qt_version() {
        return qVersion();
    }
}