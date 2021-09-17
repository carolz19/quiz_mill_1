# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.10.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Convert Jupyter notebooks to Canvas quizzes
# This guide shows you how you go from Jupyter notebooks to generating multiple quizzes and sending them to Canvas. The following steps allow you to run the commands in the notebook (on a JupyterHub), but simply copy and paste the commands in your terminal if running on your local machine.
# ***
# ## Prerequisites:
# - Must have the Canvas API token
# - Must have the base notebook
#
# ## Step 1: Remove any old "Two Layers" quizzes from Canvas (if applicable)
# Run the following cell:

# %% language="bash"
# remove -v ..

# %% [markdown]
# ### Output should be similar to the following:
# ![remove output](output_remove_canvas.png)

# %% [markdown]
# ## Step 2: Remove any old notebooks from `output/` folder (if applicable)
# Run the following cell:

# %% language="bash"
# clean -v

# %% [markdown]
# ### Output should be similar to the following:
# ![clean output](output_clean.png)

# %% [markdown]
# ## Step 3: Generate **N** notebooks with random parameters
# Run the following cell:

# %% language="bash"
# N=5
# generate -n $N notebooks/

# %% [markdown]
# ### Expected output:
# ![generate notebooks expected output](output_generate.png)
#
# ### What the notebook should look like:
# See an example [here](ex_two_layers.md).  
# The notebooks are located at `quiz_mill/notebooks/output/unfiltered/`.

# %% [markdown]
# ## Step 4: Filter notebooks into student and solution notebook versions
# Run the following cell:

# %% language="bash"
# filter -v notebooks/output

# %% [markdown]
# ### Expected output:
# ![filter notebook](output_filter.png)
#
# ### Student notebook:
# See [here](ex_output_two_layers1_student.md) for an example student notebook.
#
# ### Solution notebook:
# See [here](ex_output_two_layers1_solution.md) for an example solution notebook.

# %% [markdown]
# ### Step 5: Send solution notebooks as quizzes to Canvas
# Run the following cell:

# %% language="bash"
# send -c 51824 -v notebooks/output/filtered/solution/

# %% [markdown]
# ### Expected output:
# ![to-canvas output](out_to_canvas.png)
#
# ### What you should see on Canvas:
# ![quizzes on Canvas](canvas_quizzes.png)

# %% [markdown]
# See the [reference](reference.ipynb) guide for full details of commands and options.
