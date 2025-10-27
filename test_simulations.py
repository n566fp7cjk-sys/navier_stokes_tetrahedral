import numpy as np
import matplotlib.pyplot as plt
from src.triangular_navier_stokes import TriangularNavierStokes, taylor_green_vortex_2d

def test_L_T_1():
    sim = TriangularNavierStokes(L_T=1.0, nu=0.01)
    taylor_green_vortex_2d(sim, t=0)
    dt = 0.01
    n_steps = int(0.5 / dt)
    
    print(f"L_T = 1.0, Nodes: {sim.n_vertices}, dt = {dt:.6f}, n_steps = {n_steps}")
    omega0 = sim.compute_max_vorticity()
    E0 = sim.compute_energy()
    print(f"Initial vorticity: {omega0:.6f}")
    print(f"Initial energy: {E0:.6f}")
    
    omega_history = [omega0]
    time_history = [0]
    
    for step in range(n_steps):
        sim.step(dt)
        if step % max(1, n_steps // 10) == 0:
            t = (step + 1) * dt
            omega_t = sim.compute_max_vorticity()
            omega_history.append(omega_t)
            time_history.append(t)
            print(f"t={t:.3f}, vorticity={omega_t:.6f}, div={sim.compute_max_divergence():.6f}")
    
    omega_final = sim.compute_max_vorticity()
    E_final = sim.compute_energy()
    print(f"Final vorticity (t=0.5): {omega_final:.6f}")
    print(f"Final energy (t=0.5): {E_final:.6f}")
    growth_ratio = omega_final / omega0
    print(f"Vorticity growth ratio: {growth_ratio:.4f}")
    
    plot_vorticity(sim, time_history, omega_history)
    plot_vorticity_field(sim)
    sim.test_diffusion_enhanced()
    
    return omega_history, time_history, E0, E_final

def plot_vorticity(sim, time_history, omega_history):
    plt.figure(figsize=(10, 6))
    plt.plot(time_history, omega_history, 'b-', label='Vorticity')
    plt.xlabel('Time')
    plt.ylabel('Vorticity')
    plt.title('Vorticity Evolution')
    plt.legend()
    plt.grid(True)
    plt.savefig('plots/vorticity_evolution_L_T_1.0.png')
    plt.close()

def plot_vorticity_field(sim):
    plt.figure(figsize=(10, 6))
    plt.tricontourf(sim.positions[:, 0], sim.positions[:, 1], sim.triangles, sim.compute_max_vorticity(), cmap='viridis')
    plt.colorbar(label='Vorticity')
    plt.title('Vorticity Field at t=0.5')
    plt.savefig('plots/vorticity_field_L_T_1.0.png')
    plt.close()

if __name__ == "__main__":
    test_L_T_1()
