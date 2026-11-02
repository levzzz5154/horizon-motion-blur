// Motion blur's settings page.
fn motion_blur_page(mod_id: &str, buttons: &mut Vec<String>) {
    use horizon_client::gfx::native_render::motion_blur as mb;
    if mod_id == mb::ID {
        buttons.extend(mb::settings().labels());
    }
}
