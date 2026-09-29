import gradio as gr
import numpy as np
from wave_dispersion_calculator import solve_dispersion, compute_ursell, generate_dispersion_curve

def compute(T, d, H):
    k, L, c, cg, wl_class = solve_dispersion(T, d)
    # Ursell classification if H > 0
    if H > 0:
        Ur, ursell_class = compute_ursell(k, d, H)
    else:
        Ur = np.nan
        ursell_class = "N/A (H=0)"
    # Generate dispersion curve figure
    fig = generate_dispersion_curve(T, d)
    return (
        round(k, 4),
        round(L, 2),
        round(c, 2),
        round(cg, 2),
        wl_class,
        round(Ur, 4) if not np.isnan(Ur) else "N/A",
        ursell_class,
        fig
    )

with gr.Blocks(title="Wave Dispersion Calculator") as demo:
    gr.Markdown("# Wave Dispersion Calculator")
    with gr.Row():
        with gr.Column():
            T = gr.Slider(minimum=1., maximum=30., step=0.1, value=10., label="Wave period T (s)")
            d = gr.Slider(minimum=0.1, maximum=5000., step=0.1, value=10., label="Water depth d (m)")
            H = gr.Number(minimum=0., maximum=100., step=0.1, value=1., label="Wave height H (m) (optional for Ursell)")
            btn = gr.Button("Compute")
        with gr.Column():
            k_out = gr.Textbox(label="Wavenumber k (rad/m)")
            L_out = gr.Textbox(label="Wavelength L (m)")
            c_out = gr.Textbox(label="Phase speed c (m/s)")
            cg_out = gr.Textbox(label="Group velocity cg (m/s)")
            wl_class_out = gr.Textbox(label="Water depth classification")
            Ur_out = gr.Textbox(label="Ursell number Ur")
            ursell_class_out = gr.Textbox(label="Ursell classification")
    plot = gr.Plot(label="Dispersion curve (phase speed vs period)")

    btn.click(fn=compute, inputs=[T, d, H], outputs=[k_out, L_out, c_out, cg_out, wl_class_out, Ur_out, ursell_class_out, plot])

demo.launch(server_name="0.0.0.0", server_port=7860)
