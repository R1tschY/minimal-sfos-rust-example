

fn main() {
    let qt5core = pkg_config::probe_library("Qt5Core").unwrap();

    cc::Build::new()
        .cpp(true)
        .includes(qt5core.include_paths)
        .file("src/lib.cpp")
        .compile("myffi");
}