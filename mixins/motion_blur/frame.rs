// Hands the kept settings and the Options > Mods switch to the renderer's half.
fn motion_blur_frame(game: &mut crate::game::Game<'_>) {
    use horizon_client::gfx::native_render::motion_blur as mb;
    if !mb::loaded() {
        let game = &*game;
        mb::set_settings(mb::Settings::read(|key| game.native_setting(mb::ID, key)));
    }
    mb::set_on(game.native_on(mb::ID));
}
