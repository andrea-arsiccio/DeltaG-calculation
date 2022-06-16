# DeltaG-calculation

The python script DeltaG-calculation.py can be used to compute transfer free energies that describe the transfer of a protein from water at 298 K and 1 bar to different osmolyte solutions [1], at any temperature [2] and pressure [3] value.

Usage:

python3 DeltaG-calculation.py osmolyte-type osmolyte-concentration T-value T-approach P

where:

osmolyte-type: can be sucrose, urea, TMAO, proline, betaine or none. In all cases, free-energy values extracted from the work by Auton, Bolen and coworkers are employed [4].

osmolyte-concentration: concentration of the selected osmolyte, in M.

T-value: temperature value, in K.

T-approach: can be 2 or 3. Refers to the approaches for the inclusion of temperature effects in implicit solvent simulations described in [2].

P: pressure value, in bar. 

Example:

python3 DeltaG-calculation.py sucrose 1 310 2 3500 

computes the free energies of transfer for a protein in 1M sucrose, at 310 K (using approach 2 as described in [2]) and 3500 bar.

The output is a file DeltaG.dat in the form:


ALA -7.940509280346168

ARG -19.960373360467845

ASN -9.99407582569926

ASP -9.572109106534343

CYS -9.364199656150657

GLN -13.07462625784209

GLU -12.722932211587958

GLY 0.0

HIS -15.096255879863905

ILE -14.636274953571094

LEU -14.441369734200844

LYS -16.454656919057342

MET -14.530093336954897

PHE -18.306281355966355

PRO -10.06821859745863

SER -6.040322322443721

THR -10.827620080746481

TRP -24.170822666260406

TYR -19.230771559742372

VAL -12.257909976433293

BACKBONE -4.712050450690486


where free energy of transfer values, in kJ/mol, are provided for each sidechain/backbone. The output is compatible for use with the SASA module of Plumed (https://www.plumed.org/doc-v2.8/user-doc/html/_s_a_s_a_m_o_d.html).

REFERENCES:

[1] Arsiccio, Andrea; Ganguly, Pritam; Shea, Joan-Emma (2022): A Transfer Free Energy Based Implicit Solvent Model for Protein Simulations in Solvent Mixtures: Urea-Induced Denaturation as a Case Study. In The Journal of Physical Chemistry B. DOI: 10.1021/acs.jpcb.2c00889

[2] Arsiccio, Andrea; Shea, Joan-Emma (2021): Protein Cold Denaturation in Implicit Solvent Simulations: A Transfer Free Energy Approach. In The Journal of Physical Chemistry B 125 (20), pp. 5222–5232. DOI: 10.1021/acs.jpcb.1c01694.

[3] Arsiccio, Andrea; Shea, Joan-Emma (2021a): Pressure Unfolding of Proteins: New Insights into the Role of Bound Water. In The Journal of Physical Chemistry B 125 (30), pp. 8431–8442. DOI: 10.1021/acs.jpcb.1c04398.

[4] Auton, Matthew; Bolen, D. Wayne (2007): Application of the Transfer Model to Understand How Naturally Occurring Osmolytes Affect Protein Stability. In D. Häussinger, H. Sies (Eds.): Methods in enzymology. Volume 428, Osmosensing and osmosignaling, vol. 428. Amsterdam, New York: Elsevier (Methods in Enzymology, v. 428), pp. 397–418.
