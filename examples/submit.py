# -*- coding: utf-8 -*-
"""Submit a test calculation on localhost.

Usage: verdi run submit.py

Note: This script assumes you have set up computer and code as in README.md.
"""
import os

# use code name specified using 'verdi code setup'
code = Code.get_from_string('zeopp')

# use computer name specified using 'verdi computer setup'
computer = Computer.get('localhost')

# Prepare input parameters
NetworkParameters = DataFactory('zeopp.parameters')
parameters = NetworkParameters({'cssr': True})
SinglefileData = DataFactory('singlefile')
inputfile = SinglefileData(file=os.path.abspath('HKUST-1.cif'))

# set up calculation
calc = code.new_calc()
calc.label = "aiida_zeopp format conversion"
calc.description = "Test converting .cif to .cssr format"
calc.set_max_wallclock_seconds(1 * 60)
# This line is only needed for local codes, otherwise the computer is
# automatically set from the code
calc.set_computer(computer)
calc.set_withmpi(False)
calc.set_resources({"num_machines": 1})
calc.use_parameters(parameters)
calc.use_input_structure(inputfile)

calc.store_all()
calc.submit()
print("submitted calculation; calc=Calculation(uuid='{}') # ID={}"\
        .format(calc.uuid,calc.dbnode.pk))
