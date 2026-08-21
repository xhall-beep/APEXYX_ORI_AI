#!/data/data/com.termux/files/usr/bin/bash
# APEXYX_ORI_AI — on-device (Termux) APK build.
#
# WHY THIS SCRIPT EXISTS
# The build was halted by:
#   thread_pthread.h:483: call to undeclared function 'sem_clockwait'
#   [-Werror=implicit-function-declaration]
# That failure is in the HOST python (hostpython3), compiled by the Termux
# toolchain — NOT the Android target. buildozer.spec's android.p4a_extra_args
# only reliably reaches target recipes, so we ALSO export CFLAGS here so the
# flag reaches the hostpython3 compile. This is the line that actually unblocks
# the build on-device.
set -euo pipefail

export CFLAGS="${CFLAGS:-} -Wno-error=implicit-function-declaration"
export CPPFLAGS="${CPPFLAGS:-} -Wno-error=implicit-function-declaration"

echo "[apexyx] CFLAGS=$CFLAGS"
echo "[apexyx] starting buildozer android debug ..."
buildozer android debug "$@"
