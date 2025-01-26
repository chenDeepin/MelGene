### **Steps to Create the Conda Environment:**

1. **Create the Environment:**
   Run the following command to create a Conda environment using the `requirements.txt` file:

   ```bash
   conda create --name melgene_env --file requirements.txt
   ```

2. **Activate the Environment:**
   Activate the environment using:

   ```bash
   conda activate melgene_env
   ```

3. **Install Additional Packages (if needed):**
   If you need to install additional packages, you can do so using:

   ```bash
   conda install <package_name>
   ```

   Or, if the package is not available in Conda, use `pip`:

   ```bash
   pip install <package_name>
   ```

4. **Deactivate the Environment:**
   When you’re done, deactivate the environment using:

   ```bash
   conda deactivate
   ```

---

### **Optional Dependencies:**

If you plan to extend the project with additional features, you might need:

- **`matplotlib`:** For visualizing data (e.g., codon frequencies or pitch distributions).
- **`scipy`:** For advanced mathematical operations.
- **`pandas`:** For handling tabular data (e.g., codon frequency tables).