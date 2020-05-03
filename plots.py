import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

plt.style.use('ggplot')

###################################
# potential outcome decomposition #
###################################
_, ax = plt.subplots(figsize=(8, 4), sharex='col', sharey='col')
ax.plot([0, 1], [1, 2], linestyle='-', color='k', label='control')
ax.plot([0, 1], [1, 4], linestyle='-', color='k', label='treatment')

plt.vlines(x=1, ymin=2, ymax=4, alpha=0.5)
plt.text(1.02, 3.03, '$\delta$', fontsize=14)

plt.vlines(x=1, ymin=1, ymax=2, alpha=0.5)
plt.text(1.02, 1.5, '$\\tau$', fontsize=14)

ax.set_xticks([0, 1])
ax.set_yticks([1, 2, 4])

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)


def formatter(value, tick_number):
    if value == 1:
        return '$Y_0^a \equiv \\alpha$'
    elif value == 2:
        return '$Y_1^1$'
    elif value == 4:
        return '$Y_1^0$'
    else:
        return None


ax.yaxis.set_major_formatter(plt.FuncFormatter(formatter))
ax.set_xlabel('time', fontsize=14)

plt.ylim(0.5, 4.5)
plt.xlim(-.05, 1.075)
plt.tight_layout()
plt.savefig('images/decomposition.png', format='png', bbox_inches='tight')


####################
# compatible areas #
####################
_, ax = plt.subplots(figsize=(8, 4))

x = np.linspace(0, 1.6, 100)
y0 = [-1 for _ in range(100)]
y1 = [1 for _ in range(100)]

ax.fill_between(x, y0, y1, facecolor='grey', interpolate=True, alpha=0.5)
plt.text(0.5, 0, '$\\frac{\sigma_\delta}{\sigma_\\tau} = \\sqrt{r+\\rho^2} - \\rho$', fontsize=14)

x = np.linspace(-1, 0, 100)
y0 = [-1 for _ in range(100)]
y1 = -np.sqrt(-x)
ax.fill_between(x, y0, y1, facecolor='grey', interpolate=True, alpha=0.5)

x = np.linspace(-1, 0, 100)
y0 = [-1 for _ in range(100)]
y1 = -np.sqrt(-x)
ax.fill_between(x, y0, y1, facecolor='blue', interpolate=True, alpha=0., hatch='/')

plt.text(-0.95, -0.4, '$\\frac{\sigma_\delta}{\sigma_\\tau} = |\\rho| -\\sqrt{\\rho^2 - |r|} $', fontsize=14)

ax.set_yticks([-1, -.5, 0, .5, 1])
ax.set_xlabel('$r = \\nu^2 - 1$', fontsize=14)

ax.set_ylabel('$\\rho$', fontsize=14, rotation=0)

plt.ylim(-1.1, 1.1)
plt.xlim(-1.1, 1.6)
plt.tight_layout()
plt.savefig('images/compatible_areas.png', format='png', bbox_inches='tight')


##########################################
# Standard deviation of treatment effect #
##########################################
colors = list(cm.rainbow(np.linspace(0, 0.2, 4))) + list(cm.rainbow(np.linspace(0.75, 1, 5)))

_, ax = plt.subplots(figsize=(8, 5), sharex='col', sharey='col')

j = -1
for r in [-0.85, -0.65, -0.25, -0.025]:
    j += 1
    x = np.linspace(-1, -np.sqrt(-r), 200)
    y = np.sqrt(x ** 2 + r) - x
    nu = np.sqrt(1 + r)
    ax.plot(x, y, color=colors[j], label=f'$\\nu={nu:.2}$')

    y = - np.sqrt(x ** 2 + r) - x
    ax.plot(x, y, color=colors[j])

x = np.linspace(-1, -0.001, 100)
y = - x

ax.set_xticks([-1, -.5, 0, .5, 1])
ax.set_yticks([0, 1, 2])

ax.plot(x, y, linestyle='--', color='k', alpha=0.3)

x = np.linspace(-1, 1, 100)
r = 0.0
nu = np.sqrt(1 + r)
y = np.sqrt(x ** 2) - x
ax.plot(x, y, label=f'$\\nu={nu:.2}$', color='k')

x = np.linspace(-1, 1, 100)
for r in [0.15, 0.3, 0.5, 1.0, 1.5]:
    j += 1
    nu = np.sqrt(1 + r)
    y = np.sqrt(r + x ** 2) - x
    ax.plot(x, y, label=f'$\\nu={nu:.2}$', color=colors[j])

ax.set_xticks([-1, -.5, 0, .5, 1])
ax.set_yticks([0, 1, 2])
ax.legend()

ax.set_ylabel('$\\frac{\sigma_\delta}{\sigma_\\tau}$', fontsize=14, rotation=0)
ax.set_xlabel('$\\rho$', fontsize=14)
ax.legend()

ax.set_ylabel('$\\frac{\sigma_\delta}{\sigma_\\tau}$', fontsize=14, rotation=0)
ax.set_xlabel('$\\rho$', fontsize=14)
plt.savefig('images/norm_sd_te.png', format='png', bbox_inches='tight')


##########################
# Compatible area bounds #
##########################
fig, ax = plt.subplots(figsize=(8, 4), sharex='col', sharey='col')

a = 0.25
nu_lb, nu_ub = np.sqrt(1 - a), np.sqrt(1 + a)

r = -a
x = np.linspace(-1, -np.sqrt(-r), 100)
y = np.sqrt(x ** 2 + r) - x
ax.plot(x, y, color='k')

y = - np.sqrt(x ** 2 + r) - x
ax.plot(x, y, color='k')

ax.set_xticks([-1, -.5, 0, .5, 1])
ax.set_yticks([0, 1, 2])

ax.plot(x, y, linestyle='--', color='k', alpha=0.3)

x = np.linspace(-1, 1, 100)
r = a
y = np.sqrt(r + x ** 2) - x
ax.plot(x, y, color='k')

ax.set_xticks([-1, -.5, 0, .5, 1])
ax.set_yticks([0, 1, 2])
ax.set_ylabel('$\\frac{\sigma_\delta}{\sigma_\\tau}$', fontsize=14, rotation=0)
ax.set_xlabel('$\\rho$', fontsize=14)
plt.text(-0.48, .25, f'${nu_lb:.2} < \\nu < {nu_ub:.2}$', fontsize=14)

ax.set_ylabel('$\\frac{\sigma_\delta}{\sigma_\\tau}$', fontsize=14, rotation=0)
ax.set_xlabel('$\\rho$', fontsize=18)
plt.savefig('images/compatible_area_bound.png', format='png', bbox_inches='tight')


####################
# Fixed rho curves #
####################
_, ax = plt.subplots(figsize=(8, 5), sharex='col', sharey='col')

colors = list(cm.rainbow(np.linspace(0, 0.2, 5))) + list(cm.rainbow(np.linspace(0.75, 1, 3)))

j = -1
for rho in [-1.0, -0.9, -0.7, -0.5, -0.25]:
    j += 1
    r = np.linspace(- rho ** 2, 0., 100)
    nu = np.sqrt(1 + r)
    y = -np.sqrt(r + rho ** 2) - rho
    ax.plot(nu, y, color=colors[j])

j = -1
for rho in [-1.0, -0.9, -0.7, -0.5, -0.25, 0.0, 0.5, 1.0]:
    j += 1
    r = np.linspace(0 if rho >= 0 else -rho ** 2, 1.3, 100)
    nu = np.sqrt(1 + r)
    y = np.sqrt(r + rho ** 2) - rho
    ax.plot(nu, y, label=f'$\\rho={rho}$', color=colors[j] if rho != 0 else 'k')

ax.set_xticks([0, .5, 1, 1.5])
ax.set_yticks([0, 1, 2])
ax.legend()

ax.set_ylabel('$\\frac{\sigma_\delta}{\sigma_\\tau}$', fontsize=14, rotation=0)
ax.set_xlabel('$\\nu$', fontsize=14)
plt.savefig('images/fixed_rho_curves.png', format='png', bbox_inches='tight')

plt.close()
