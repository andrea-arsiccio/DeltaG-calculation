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


ALA -5.104509280346155

ARG -18.022773360467813

ASN -10.01247582569926

ASP -9.370189106534346

CYS -7.65219965615061

GLN -11.410626257842102

GLU -12.162132211587958

GLY 0.0

HIS -12.518655879863887

ILE -10.281074953571013

LEU -10.972569734200743

LYS -15.13385691905735

MET -11.972493336954917

PHE -14.155881355966365

PRO -8.078618597458634

SER -5.978722322443723

THR -8.435620080746514

TRP -18.04282266626059

TYR -14.412371559742487

VAL -9.144309976433274

BACKBONE -3.1598904506905


where free energy of transfer values, in kJ/mol, are provided for each sidechain/backbone. The output is compatible for use with the SASA module of Plumed (https://www.plumed.org/doc-v2.8/user-doc/html/_s_a_s_a_m_o_d.html).

REFERENCES:

[1] Arsiccio, Andrea; Ganguly, Pritam; Shea, Joan-Emma (2022): A Transfer Free Energy Based Implicit Solvent Model for Protein Simulations in Solvent Mixtures: Urea-Induced Denaturation as a Case Study. In The Journal of Physical Chemistry B 126 (24), pp. 4472–4482. DOI: 10.1021/acs.jpcb.2c00889.

[2] Arsiccio, Andrea; Shea, Joan-Emma (2021): Protein Cold Denaturation in Implicit Solvent Simulations: A Transfer Free Energy Approach. In The Journal of Physical Chemistry B 125 (20), pp. 5222–5232. DOI: 10.1021/acs.jpcb.1c01694.

[3] Arsiccio, Andrea; Shea, Joan-Emma (2021a): Pressure Unfolding of Proteins: New Insights into the Role of Bound Water. In The Journal of Physical Chemistry B 125 (30), pp. 8431–8442. DOI: 10.1021/acs.jpcb.1c04398.

[4] Auton, Matthew; Bolen, D. Wayne (2007): Application of the Transfer Model to Understand How Naturally Occurring Osmolytes Affect Protein Stability. In D. Häussinger, H. Sies (Eds.): Methods in enzymology. Volume 428, Osmosensing and osmosignaling, vol. 428. Amsterdam, New York: Elsevier (Methods in Enzymology, v. 428), pp. 397–418.
