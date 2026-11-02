// Entity runs and the world's depth, while the blur draws.
fn motion_blur_needs(needs: &mut crate::gfx::native_render::RenderNeeds) {
    if crate::gfx::native_render::motion_blur::active() {
        needs.entity_spans = true;
        needs.world_depth = true;
    }
}
