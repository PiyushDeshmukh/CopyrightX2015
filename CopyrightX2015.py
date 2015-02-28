import os

url = "http://wilkins.law.harvard.edu/courses/CopyrightX2015/"
os.mkdir("CopyrightX2015")
os.chdir("CopyrightX2015")
A = [("The Foundations of Copyright Law", 4), ("Fairness and Personality Theories", 3), ("The Subject Matter of Copyright", 6), ("Welfare Theory", 3), ("Authorship", 3), ("The Mechanics of Copyright", 3), ("The Rights to Reproduce and Modify", 3), ("The Rights to Distribute, Perform, and Display", 3), ("Fair Use", 3), ("Cultural Theory", 3), ("Supplements to Copyright: Secondary Liability and Para-copyright", 3), ("Remedies", 3)]
file_type = "_low.mp4"
length = len(A)
array = ["Introduction", "The System of Multilateral Treaties", "Originality", "The Idea/Expression Distinction", "Introduction", "Fairness", "Personality", "Literary Works (and software)", "Dramatic Works (and choreography)", "Music", "Audiovisual Works", "Fictional Characters", "Visual and Architectural Works", "The Utilitarian Framework", "The Incentive Theory of Copyright", "Applications and Assessment", "Sole Authorship", "Joint Authorship", "Works for Hire", "The Decline of Formalities", "Duration", "Protective Provisions", "Reproduction", "Improper Appropriation", "Derivative Works", "Distribution", "Public Performances", "Exceptions and Limitations", "The History of Fair Use", "Fair Use Today", "Other Approaches", "Premises", "Implications", "Supplements and Concerns", "Secondary Liability", "Dual-Use Technologies", "Technological Protection Measures", "Equitable Relief", "Damages", "Criminal Penalties"]
index = 0
for ele in range(length):
     if ele > 9:
          folder = str(ele + 1) + " - " + A[ele][0]
     else:
          folder = "0" + str(ele + 1) + " - " + A[ele][0]
     os.mkdir(folder)
     os.chdir(folder)
     for i in range(1,A[ele][1]+1):
          inside_folder_name = str(ele + 1) + "." + str(i) + " - " + array[index]
          os.mkdir(inside_folder_name)
          os.chdir(inside_folder_name)
          os.system("wget " + url + str(ele + 1) + "." + str(i) + file_type)
          os.chdir("..")
          index += 1
     os.chdir("..")
     
