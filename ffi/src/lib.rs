use std::os::raw::c_char;

extern "C" {
  pub fn qt_version() -> *const c_char;
}