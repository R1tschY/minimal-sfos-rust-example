use std::ffi::CStr;
use ffi::qt_version;


fn main() {
  unsafe {
    let slice = CStr::from_ptr(qt_version());
    println!("Hello World: {:?}", slice);
  }
}
