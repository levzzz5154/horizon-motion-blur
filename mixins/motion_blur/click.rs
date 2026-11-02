// A click on motion blur's settings page: the next choice, in effect at once and kept.
fn motion_blur_click(game: &mut crate::game::Game<'_>, mod_id: &str, button: usize) {
    use horizon_client::gfx::native_render::motion_blur as mb;
    if mod_id != mb::ID {
        return;
    }
    let mut settings = mb::settings();
    settings.click(button);
    mb::set_settings(settings);
    for (key, value) in settings.stored() {
        game.native_set_setting(mb::ID, key, &value);
    }
}
