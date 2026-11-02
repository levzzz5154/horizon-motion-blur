// The world is drawn: blur it.
fn motion_blur_world_drawn(world: &mut crate::gfx::native_render::WorldDrawn<'_>) {
    crate::gfx::native_render::motion_blur::world_drawn(world);
}
