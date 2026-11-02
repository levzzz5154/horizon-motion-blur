// Motion blur's row in Options > Mods.
fn motion_blur_listed(mods: &mut Vec<crate::game::native_hooks::NativeMod>) {
    use horizon_client::gfx::native_render::motion_blur as mb;
    mods.push(crate::game::native_hooks::NativeMod {
        id: mb::ID.into(),
        title: format!("Motion Blur {}", mb::VERSION),
        description: mb::DESCRIPTION.into(),
        keys: Vec::new(),
    });
}
