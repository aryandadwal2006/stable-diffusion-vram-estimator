def f(h: int, w: int, prompt_length: int, **kwargs):
    model_weights = 2048 
    framework_overhead = 600 
    pixel_area = h * w
    base_activation_memory = 18.53 * pixel_area / (1024**2)
    prompt_factor = max(1.0, prompt_length / 77.0)
    attention_memory = 1.3 * pixel_area / (1024**2) * prompt_factor
    total_vram = model_weights + framework_overhead + base_activation_memory + attention_memory
    return total_vram

