use std::ffi::CStr;
use std::os::raw::c_char;

extern "C" {
  fn qt_version() -> *const c_char;
}


fn main() {
  unsafe {
    let slice = CStr::from_ptr(qt_version());
    println!("Hello World: {:?}", slice);
  }
}
