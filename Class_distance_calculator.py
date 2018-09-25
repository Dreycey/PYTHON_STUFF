# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 01:33:40 2018

@author: Dreycey
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt; plt.rcdefaults()


# Constructing Position Matrix
# H_list_1 = [[x1,y1,z1],[x2,y2,z2],[x3,y3,z3],[x4,y4,z4],[x5,y5,z5],.....]

class rna_model(object):

    def __init__(self, pdf = 0, Larmord_chemical_shifts_file = 0, specified_distance = 2):
        self.tangerine = 'and now a thousand years pass'
        self.graph_type = 0
        self.specified_distance = specified_distance
        self.energyfilename = 'no name'
        self.model_name = 'Specify model_name' 
        self.bincount = 50
        self.figure_width = 10
        self.figure_height = 10
        self.outline_width_scatter= 0.5
        if pdf != 0:
            self.pdf = pdf
        else: 
            print ('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print ('!!WARNING: NO PDF SUPPLIED')
            print ("!!Certain functions won't work!")
            print ('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n')
        if Larmord_chemical_shifts_file != 0:
            self.Larmord_chemical_shifts_file = Larmord_chemical_shifts_file
        else: 
            print ('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            print ('!!WARNING: NO CHEMICAL SHIFT FILE SUPPLIED')
            print ("!!Certain functions won't work!")
            print ('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n')   
            
        self.position_matrix, self.name_matrix  = self.position_matrix()
        #self.ayyy = self.position_matrix
        self.distance_matrix = self.distance_matrix()
        self.residuedistancematrix = self.residuedistancematrix()
        self.noesy_interactions = self.larmorD_simRNA()
        self.H_shifts_1_2, self.H_shifts_1_3, self.residue_number_2, self.residue_number_3 = self.larmorDprocessing()
        
    def position_matrix(self):
        
        pdf = self.pdf
        file = open(pdf, "r") #open pdb
               #take rows of pdb with specified hydrogens
               #map name of hydrogens into a 1D matrix 
               #map X, Y, and Z coordinates into a ix3 matrix, corresponding to name matrix
        lines = file.readlines()
        '''
        for i in lines: 
            lines = i.split()
            #print(lines)
        '''
        distance_m = [] #This contains the rows of the PDB file
        
        for i in lines: 
            lines = i.split()
            distance_m.append(lines)
            
    ##ONLY EDIT BELOW THIS POINT!
        H_counter = 0 
        H_matrix_temp = []
        H_position_matrix = []
        for i in range(0, (len(distance_m) - 1 )):
            name_matrix_temp = []
            name_matrix_temp.append(distance_m[i][2])
            #print (distance_m[i][2])
            #print(name_matrix_temp)
            if distance_m[i][2][0] == 'H':
                H_counter = H_counter + 1 #leave this alone
                H_name_matrix = distance_m[i][5] + '_' + distance_m[i][3] + '_' + distance_m[i][2]
                H_matrix_temp.append(H_name_matrix)
                H_position_matrix.append([distance_m[i][6], distance_m[i][7], distance_m[i][8]])
        
        
        print ('There are ' + str(H_counter) + ' hydrogens in the model')
        print ('READING PDF RESULTS:')
        print ('The name matrix is ' + str(len(H_matrix_temp)) + ' rows long')
        print ('The distance matrix is ' + str(len(H_position_matrix)) + ' rows long')
                
        position_matrix =  H_position_matrix 
        name_matrix =  H_matrix_temp 
        
        return position_matrix, name_matrix
    
    
    #Constructing Distance Matrix
    def distance_matrix(self):
        position_matrix = self.position_matrix
        name_matrix = self.name_matrix
        
        distance_matrix = []
        res_counter = 0 - 1
        x_matrix = []
        y_matrix = []
        z_matrix = []
        dx_matrix = []
        dy_matrix = []
        dz_matrix = []
    
        #Make 1D vectors for X, Y, and Z coordinates
        for i in position_matrix:
            res_counter = res_counter + 1
            for j in range(0, 3):
    
                if j == 0:
                    #print ('x coordinate' + ' for: ' + name_matrix[res_counter] + ' is ' + position_matrix[res_counter][j])
                    x_matrix.append(position_matrix[res_counter][j])
                elif j == 1:
                    #print ('y coordinate' + ' for: ' + name_matrix[res_counter] + ' is ' + position_matrix[res_counter][j])
                    y_matrix.append(position_matrix[res_counter][j])
                elif j == 2:
                    #print ('z coordinate' + ' for: ' + name_matrix[res_counter] + ' is ' + position_matrix[res_counter][j])
                    z_matrix.append(position_matrix[res_counter][j])
        
        #Make difference Matrices: dx, dy, dz
        print ('Please wait while distances between hydrogens is calculated..')
        for i in range(0, len(x_matrix)):
            dx_row_temp_vector = []
            dy_row_temp_vector = []
            dz_row_temp_vector = []
            for j in range(0, len(x_matrix)):
                dx = abs(float(x_matrix[i]) - float(x_matrix[j]))
                dy = abs(float(y_matrix[i]) - float(y_matrix[j]))
                dz = abs(float(z_matrix[i]) - float(z_matrix[j]))
                dx = format(float(dx), '.2f')
                dy = format(float(dx), '.2f')
                dz = format(float(dx), '.2f')
                dx_row_temp_vector.append(dx)
                dy_row_temp_vector.append(dy)
                dz_row_temp_vector.append(dz)
            #add temp 1D vectors to make NxN matrix           
            dx_matrix.append(dx_row_temp_vector)
            dy_matrix.append(dy_row_temp_vector)
            dz_matrix.append(dz_row_temp_vector)
    
    
        #Making Distance Matrix using values from difference matrices
        print ('Please wait while distance matrix is constructed..')
        for i in range(0, len(x_matrix)):
            distance_row_temp_vector = []
            for j in range(0, len(x_matrix)):
                dx = float(dx_matrix[i][j])
                dy = float(dy_matrix[i][j])
                dz = float(dz_matrix[i][j])
                distance = ( (dx)**2 + (dy)**2 + (dz)**2 )**(0.5) #pythagorean theorem
                distance_row_temp_vector.append(distance)
            distance_matrix.append(distance_row_temp_vector)
            
        
        return distance_matrix
                
      
    def makingplots(self):
        print ('Please wait while graphs are constructed..')
        
        distance_matrix = self.distance_matrix
        name_matrix = self.name_matrix
        residuedistancematrix = self.residuedistancematrix
        graph_type = self.graph_type
        
        
        distance_matrix = np.array(distance_matrix)
        residuedistancematrix = np.array(residuedistancematrix)
        
        if graph_type == 0:
            print (' \n MUST INCLUDE GRAPH TYPE')
            print ('Either specified as "residue" or "full"')
            print ("for example, type: object_1.graph_type='full' \n")
            
        elif graph_type == 'residue':
            fig, ax = plt.subplots()
            im = ax.imshow(residuedistancematrix)
            # Create colorbar
            cbar = ax.figure.colorbar(im, ax=ax)
            cbar.ax.set_ylabel('distance label \n (Angstroms)', rotation=-90, size = 15, va="bottom")
        
            # Rotate the tick labels and set their alignment.
            plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
            ax.set_title("Average Hydrogen Distance Per Residue Matrix \n (i.e. Hydrogen-Derived Residue Contact Map)", size = 18)
            plt.ylabel('Residues in Model', size = 15)
            plt.xlabel('Residues in Model', size = 15)
            print ('Please wait.. Now printing the graph:')
            fig.tight_layout()
            plt.show()
 

        elif graph_type == 'full':
            fig, ax = plt.subplots()
            im = ax.imshow(distance_matrix)
            # Create colorbar
            cbar = ax.figure.colorbar(im, ax=ax)
            cbar.ax.set_ylabel('distance label \n (Angstroms)', rotation=-90, size = 15, va="bottom")
        
            # Rotate the tick labels and set their alignment.
            plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
            ax.set_title("Hydrogen Distance Matrix", size = 18)
            plt.ylabel('Hydrogens in Model', size = 15)
            plt.xlabel('Hydrogens in Model', size = 15)
            print ('Please wait.. Now printing the graph:')
            fig.tight_layout()
            plt.show()
 
   
    def residuedistancematrix(self): #, distance_matrix, name_matrix):
        pdf = self.pdf
        distance_matrix = self.distance_matrix
        
        hydrogens_per_res = [] #list n long, where n=# of residues
    
        file = open(pdf, "r") #open pdb
               #take rows of pdb with specified hydrogens
               #map name of hydrogens into a 1D matrix 
               #map X, Y, and Z coordinates into a ix3 matrix, corresponding to name matrix
        lines = file.readlines()
        distance_m = []
        
        for i in lines: 
            lines = i.split()
            distance_m.append(lines)
          
        #count the number of residues
        number_of_residues = 0
        for j in range(0, len(distance_m) - 1):
                if (distance_m[j][2][0] == 'H'):
                    number_of_residues = distance_m[j][5]
                else:
                    None
                    
        #Making 1D vector with number of hydrogens per residue
        for i in range(1, (int(number_of_residues) + 1)):
            counter_temp = 0
            for j in range(0, len(distance_m) - 1):
                if (distance_m[j][2][0] == 'H') and (distance_m[j][5] == str(i)):
                    counter_temp = counter_temp + 1
            hydrogens_per_res.append(counter_temp)
        
        #Making 1D vector with indexing positions
        index_positions = [0]
        indexer_counter = 0
        for i in hydrogens_per_res: 
            indexer_counter = indexer_counter + i
            index_positions.append(indexer_counter)
        
        #Making smaller matrix
        resie = []
        for I in range(0, (len(index_positions) - 1)): #for loop for BIG i
            BIG_row_temp_list = []
            for J in range(0, (len(index_positions) - 1)): #for loop for BIG J
                #The next two forloops run throught the smaler matrices
                h_distance_list_per_residue = []
                #GOING INTO SMALLER MATRIX
                for i in range(index_positions[I], index_positions[I+1]):
                   for j in range(index_positions[J], index_positions[J+1]):
                       h_distance = distance_matrix[i][j]
                       h_distance_list_per_residue.append(h_distance)
                average_h_distance = (sum(h_distance_list_per_residue) / len(h_distance_list_per_residue)) 
                BIG_row_temp_list.append(average_h_distance)
            resie.append(BIG_row_temp_list)
        
        return resie
    
    
    def larmorD_simRNA(self):
        distance_matrix = self.distance_matrix
        name_matrix = self.name_matrix
        specified_distance = self.specified_distance
        
        print (' \n Listing out important Hydrogen Interactions: \n (Below specified cutoff of ' + str(specified_distance) + ' Angstroms \n')
        new_array = [] # [Res_1, Res_2, distance]
        for i in range(len(distance_matrix)):
            for j in range(len(distance_matrix)):
                temp_list = []
                if (distance_matrix[i][j] <= specified_distance) and (name_matrix[i][0:2] != name_matrix[j][0:2]):
                    #print(distance_matrix[i][j])
                    #print(name_matrix[i])
                    #print(name_matrix[j])
                    temp_list.append(name_matrix[i])
                    temp_list.append(name_matrix[j])
                    temp_list.append(distance_matrix[i][j])
                    new_array.append(temp_list)
    
        noesy_interactions = []
        for i in range(len(new_array)):
            if ((new_array[i][0][3] == 'U' and new_array[i][0][-2:] == 'H3') or (new_array[i][0][3] == 'G' and new_array[i][0][-2:] == 'H1')) and ((new_array[i][1][3] == 'U' and new_array[i][1][-2:] == 'H3') or (new_array[i][1][3] == 'G' and new_array[i][1][-2:] == 'H1')):
                noesy_interactions.append(new_array[i])
            else:
                None
                
        noesy_interactions = np.array(noesy_interactions)
        print(noesy_interactions)
        return noesy_interactions
        
    def nmr_grapher(self):
        noesy_interactions = self.noesy_interactions
        noesy_interactions = np.array(noesy_interactions)
        noesy_interactions = noesy_interactions[noesy_interactions[:,2].argsort()]
        specified_distance =self.specified_distance
        model_name = self.model_name
        
        #BUILDING GRAPH
        row_interactions = []
        column_interactions = []
        h_interaction_distances = []
        counter_number_of_data = 0
        axis_list = []
        interaction_names = []
        
        for i in range(0, len(noesy_interactions)):
            row_interactions.append(noesy_interactions[i][0])
            
        for i in range(0, len(noesy_interactions)):
            column_interactions.append(noesy_interactions[i][1])
            
        for i in range(0, len(noesy_interactions)):        
            h_interaction_distances.append(float(noesy_interactions[i][2]))
            
        for i in range(0, len(h_interaction_distances)):
            axis_list.append(counter_number_of_data)
            counter_number_of_data = counter_number_of_data + 1
        for i in range(0, len(noesy_interactions)):        
            temp_interaction = noesy_interactions[i][0] + ' , ' + noesy_interactions[i][1]
            interaction_names.append(temp_interaction)
        
        #Making 1D bar graph of ordered distances
        plt.figure(1, figsize=(10, 10))
        y_pos = np.arange(len(interaction_names))
        plt.bar(y_pos, h_interaction_distances, color = 'r', edgecolor = 'black', align='center', alpha=0.5)
        plt.xticks(y_pos, interaction_names, rotation = 90)
        plt.ylabel('Distance (Angstroms)')
        plt.title('Distance between Hydrogrens in: ' + model_name + '\n (for specified distance of:' + ' ' + str(specified_distance) + ' Angstroms)')
         
        plt.show()
        
        ''' #THIS GRAPH WOULD BE AWESOME!
        fig = plt.figure()
        ax1 = fig.add_subplot(111, projection='3d')
    
        xpos = axis_list
        ypos = axis_list
        zpos = np.zeros(len(h_interaction_distances))
        dx = np.ones(len(h_interaction_distances))
        dy = np.ones(len(h_interaction_distances))
        dz = h_interaction_distances
    
        ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa')
        plt.show()
        '''
    
    
    
    def larmorDprocessing(self):
        file = self.Larmord_chemical_shifts_file
        file = open(file, "r")
        lines = file.readlines()
    
        residue_number = []
        residue_name = []
        hydrogen_number = []
        H_shifts_1 = []
        H_shifts_2 = []
        
        print ('\n Sorting and Plotting data from LarmorD.. \n')
        for x in lines:
            residue_number.append(x.split(' ')[2])
            residue_name.append(x.split(' ')[3])
            hydrogen_number.append(x.split(' ')[4])
            H_shifts_1.append(x.split(' ')[5])
            H_shifts_2.append(x.split(' ')[7])
        file.close()
        
        #print (residue_name)
        residue_number_2 = []
        residue_name_2 = []
        hydrogen_number_2 = []
        H_shifts_1_2 = []
        H_shifts_2_2 = []
        residue_number_3 = []
        H_shifts_1_3 = []
        H_shifts_2_3 = []
        residue_name_3 = []
        hydrogen_number_3 = []
        
        for i in range(0, len(lines)): #residue_name:
        
            if residue_name[i] == 'URA'and hydrogen_number[i] == 'H3':
                residue_number_2.append(residue_number[i])
                residue_name_2.append(residue_name[i])
                hydrogen_number_2.append(hydrogen_number[i])
                H_shifts_1_2.append(H_shifts_1[i])
                H_shifts_2_2.append(H_shifts_2[i])
            
            if residue_name[i] == 'GUA'and hydrogen_number[i] == 'H1':
                residue_number_3.append(residue_number[i])
                residue_name_3.append(residue_name[i])
                hydrogen_number_3.append(hydrogen_number[i])
                H_shifts_1_3.append(H_shifts_1[i])
                H_shifts_2_3.append(H_shifts_2[i])
    
        return H_shifts_1_2, H_shifts_1_3, residue_number_2, residue_number_3
    
    def larmorDgraphing(self):
        print ('\n Graphing prediction NOESY for RNA construct.. \n')
        H_shifts_1_2 = self.H_shifts_1_2
        H_shifts_1_3 = self.H_shifts_1_3
        residue_number_2 = self.residue_number_2
        residue_number_3 = self.residue_number_3
        noesy_interactions = self.noesy_interactions
        model_name = self.model_name
        specified_distance =self.specified_distance
        
        #combine lists
        for i in range(len(H_shifts_1_3)):
            H_shifts_1_2.append(H_shifts_1_3[i])
        for i in range(len(residue_number_3)):
            residue_number_2.append(residue_number_3[i])
    
        
        y_axis = []
        for i in range(0,len(noesy_interactions)):
            j = 0
            stoploop = 0
            while stoploop <= 1:
                if noesy_interactions[i][0][:2] == residue_number_2[j]:
                    y_axis.append(H_shifts_1_2[j])
                    stoploop = 2
                elif j == (len(residue_number_2)-1):
                    stoploop = 2
                    print ('THERE WAS A CLOSE HYDROGEN DISTANCE NOT PREDICTED IN LARMOR D, \n POSSIBLY REDUCE YOUR SPECIFIED DISTANCE CUTOFF')
                j = j + 1
                
        x_axis = []
        for i in range(0,len(noesy_interactions)):
            j = 0
            stoploop = 0
            while stoploop <= 1:
                if noesy_interactions[i][1][:2] == residue_number_2[j]:
                    x_axis.append(H_shifts_1_2[j])
                    stoploop = 2
                elif j == (len(residue_number_2)-1):
                    stoploop = 2
                    print ('THERE WAS A CLOSE HYDROGEN DISTANCE NOT PREDICTED IN LARMOR D, \n POSSIBLY REDUCE YOUR SPECIFIED DISTANCE CUTOFF')
                j = j + 1
    
        x_move = -0.2
        y_move = 0.2
        circle_size = 200
        fig, ax = plt.subplots()
        ax.scatter(H_shifts_1_2, H_shifts_1_2, facecolors='none', edgecolors='r', s = circle_size, label='chemical shift for UH3')
        ax.scatter(H_shifts_1_3, H_shifts_1_3, facecolors='none', edgecolors= 'black', s = circle_size, label='chemical shift for GH1')
        ax.scatter(y_axis, x_axis, facecolors='none', edgecolors='b', s = circle_size, label='2D chemical shift model data')
    
        plt.title('Predicted NOESY for' + ' ' +  model_name + '\n(cutoff = ' + str(specified_distance) + ' Angstroms)', size = 20)
        plt.ylabel('H1 ppm', size = 12)
        plt.xlabel('H1 ppm', size = 12)
        plt.gca().invert_xaxis()
        plt.gca().invert_yaxis()
        plt.legend(loc=2)
        
        for i in range(0,len(residue_number_2)):
            ax.annotate(residue_number_2[i], ((float(H_shifts_1_2[i]) + x_move) ,(float(H_shifts_1_2[i])) + y_move ), size = 10)
        for i in range(0,len(residue_number_3)):
            ax.annotate(residue_number_3[i], ((float(H_shifts_1_3[i]) + x_move) ,(float(H_shifts_1_3[i])) + y_move ), size = 10)
    
           
        plt.show()
    
    def energy_vs_rmsd_from_SimRNA(self): 
        print ('\n\n')
        print ('PRINTING OUT GRAPH OF ENERGY VS RMSD:')
        energyfilename = self.energyfilename
        model_name = self.model_name 
        bincount = self.bincount
        figure_width = self.figure_width
        figure_height = self.figure_height
        outline_width_scatter= self.outline_width_scatter #0.5
        
        
        if energyfilename == 'no name':
            print ('\n\nWARNING: NO FILE PATH WAS GIVEN FOR THE ENERGY vs RMSD FILE!!')
            print ("example: object_1.energyfilename = 'DENV_rmsdenergy.txt'")
            print ('ABORTING!! \n\n')
        else: 
            None
        #####################################
        #Opening data from simRNA file
        #####################################
        filename = str(energyfilename)
        model_name = str(model_name)
        file = open(filename, "r")
        lines = file.readlines()
        
        ####################################################
        #Seperating input values into energy and RMSD values
        ####################################################
        print ('\n Please wait.. ')
        print ('Seperating input values into energy and RMSD values')
        energy=[]
        rmsd=[]
        for x in lines:
            energy.append(x.split(' -')[1])
            rmsd.append(x.split(' -')[0])
        file.close()
        
        #####################################
        #Fixing input values into floats
        #update: if statements added
        #####################################
        print ('\n Please wait.. ')
        print ('Fixing input values into floats')
        rmsd_new=[]
        energy_new=[]
        #making new list of energy values
        for e in energy:
            if float(e) > 350: 
                newe = float('-'+e)
                energy_new.append(newe)
        #making new list of rmsd values
        for r in rmsd:
            if float(r) < 20:
                rmsd_new.append(float(r))
    
        #####################################
        #Plotting the ENERGY vs RMSD
        #####################################
        print ('\n Please wait.. ')
        print ('Plotting the ENERGY vs RMSD Graph')
        
        #Making the overall figure
        plt.figure(1, figsize=(figure_width,figure_height))
        plt.subplot(223)
        plt.suptitle('ENERGY versus RMSD for: ' + model_name + '\n (Bin size =  ' + str(bincount) + ')' , fontsize=16)
        plt.scatter(rmsd_new,energy_new, color='r', edgecolor = 'black', linewidths = outline_width_scatter)    
        plt.xlabel('RMSD', size='18')
        plt.ylabel('ENERGY', size='18')
    
        #Plotting the ENERGY 
        plt.subplot(224)
        plt.hist(energy_new, orientation = 'horizontal', edgecolor = 'black', bins=bincount, normed = 'True', color='r')#, linewidths = outline_width_plots)
        
        #Plotting the RMSD    
        plt.subplot(221)
        plt.hist(rmsd_new, bins=bincount, edgecolor = 'black', normed = 'True', color='r') #, linewidths = outline_width_plots)
        plt.show()









##############################################################################
# RUNNING THE PROGRAM
##############################################################################

object_1 = rna_model('ZIKA_withH.pdb', 'zika_LarmorD.txt', 3)
object_1.graph_type='residue'
object_1.model_name = 'ZIKA simRNA Model'
object_1.makingplots()
object_1.graph_type='full'
object_1.makingplots()
object_1.larmorDgraphing()
object_1.energyfilename = 'ZIKArmsdenergy.txt'
object_1.bincount = 50
object_1.energy_vs_rmsd_from_SimRNA()
object_1.nmr_grapher()



