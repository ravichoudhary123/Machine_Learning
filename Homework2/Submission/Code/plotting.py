import numpy as np
import matplotlib.pyplot as plt

# These are the "Tableau 20" colors as RGB.
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(tableau20)):
    r, g, b = tableau20[i]
    tableau20[i] = (r / 255., g / 255., b / 255.)

def plot_score_linechart(score_list, problem_instance):

    if problem_instance == 1:
        #Create values and labels for line graphs
        labels =["Score for Computer Activity","Highest score for C"]
        Depth_values = np.arange(0, len(score_list))
        #Depth_values = depth
        plt.plot(Depth_values, score_list,'or-', linewidth=3) #Plot the first series in red with circle marker
        plt.axis([0, 20, 0.9, 1])
        plt.axvline(2.0)
        #This plots the data
        plt.grid(True) #Turn the grid on
        plt.ylabel("Score") #Y-axis label
        #plt.xlabel("Hyper-parameters") #X-axis label
        #plt.xlabel("n_estimators") #X-axis label
        plt.xlabel("max_depth") #X-axis labe
        plt.title("Score vs hyperparameters for Computer Activity data") #Plot title
        plt.legend(labels,loc="best")
        #Make sure labels and titles are inside plot area
        plt.tight_layout()
        plt.savefig("../Figures/Computer_Score_line_plot.pdf")
        plt.show()
    else:
        #Create values and labels for line graphs
        labels =["Score for Housing","Highest score for C"]
        #Depth_values = np.arange(0, len(score_list))
        Depth_values = depth
        plt.plot(Depth_values, score_list,'or-', linewidth=3) #Plot the first series in red with circle marker
        plt.axis([1, 20, .60, .90])
        plt.axvline(2.0)
        #This plots the data
        plt.grid(True) #Turn the grid on
        plt.ylabel("Score") #Y-axis label
        #plt.xlabel("Hyper-parameters") #X-axis label
        #plt.xlabel("n_estimators") #X-axis label
        plt.xlabel("max_depth") #X-axis label
        plt.title("Score vs hyperparameters for Housing data") #Plot title
        plt.legend(labels,loc="best")
        #Make sure labels and titles are inside plot area
        plt.tight_layout()
        plt.savefig("../Figures/Housing_Score_line_plot.pdf")
        plt.show()