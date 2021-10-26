# Databricks notebook source
// %scala
// // ALL_NOTEBOOKS
// val tags = com.databricks.logging.AttributionContext.current.tags
// val name = tags.getOrElse(com.databricks.logging.BaseTagDefinitions.TAG_USER, java.util.UUID.randomUUID.toString.replace("-", ""))
// val username = if (name != "unknown") name else dbutils.widgets.get("databricksUsername")
// spark.conf.set("com.databricks.training.username", username)

// displayHTML("Initialized classroom variables & functions...")

# COMMAND ----------

course_name = "smlp"

username = spark.conf.get("com.databricks.training.username", "unknown-username")

dbutils.fs.mkdirs("dbfs:/user/" + username)
dbutils.fs.rm("dbfs:/user/" + username + "/" + course_name, True)
dbutils.fs.mkdirs("dbfs:/user/" + username + "/" + course_name)

base_read_path = "wasbs://courseware@dbacademy.blob.core.windows.net/machine-learning-engineering-with-databricks/scaling-machine-learning-pipelines/v01/"
london_read_path = base_read_path + "london/"
tokyo_read_path = base_read_path + "tokyo/"
base_write_path = "dbfs:/user/" + username + "/" + course_name + "/"

# Lesson 2 paths
lesson_2_path = london_read_path + "london-listings-2021-01-31-lesson-2"
lesson_2_train_path = base_write_path + "lesson_2_train_df"
lesson_2_test_path = base_write_path + "lesson_2_test_df"
lesson_2_train_prepared_path = base_write_path + "lesson_2_train_prepared_df"
lesson_2_train_feature_vector_path = base_write_path + "lesson_2_train_feature_vector_df"

lab_2_path = tokyo_read_path + "tokyo-listings-2021-01-31-lab-2"
lab_2_train_path = base_write_path + "lab_2_train_df"
lab_2_test_path = base_write_path + "lab_2_test_df"
lab_2_train_prepared_path = base_write_path + "lab_2_train_prepared_df"
lab_2_train_feature_vector_path = base_write_path + "lab_2_train_feature_vector_df"

# Lesson 3 paths
lesson_3_train_feature_vector_path = london_read_path + "london-listings-2021-01-31-lesson-3-train-feature-vector"
lesson_3_train_path = london_read_path + "london-listings-2021-01-31-lesson-3-train"
lesson_3_test_path = london_read_path + "london-listings-2021-01-31-lesson-3-test"
lesson_3_train_tree_path = london_read_path + "london-listings-2021-01-31-lesson-3-tree-train"
lesson_3_train_tree_cat_path = london_read_path + "london-listings-2021-01-31-lesson-3-train-tree-train-cat"
lesson_3_train_path_imp = london_read_path + "london-listings-2021-01-31-lesson-3-train-imputed"
lesson_3_test_path_imp = london_read_path + "london-listings-2021-01-31-lesson-3-test-imputed"

lab_3_train_path = tokyo_read_path + "tokyo-listings-2021-01-31-lab-3-train"
lab_3_test_path = tokyo_read_path + "tokyo-listings-2021-01-31-lab-3-test"

# Lesson 4 paths
lesson_4_train_path = london_read_path + "london-listings-2021-01-31-lesson-4-train"
lesson_4_test_path = london_read_path + "london-listings-2021-01-31-lesson-4-test"

lab_4_train_path = tokyo_read_path + "tokyo-listings-2021-01-31-lab-4-train"
lab_4_test_path = tokyo_read_path + "tokyo-listings-2021-01-31-lab-4-test"

# Lesson 5 paths
lesson_5_model_path = london_read_path + "london-listings-2021-01-31-lesson-5-model"
lesson_5_inference_path = london_read_path + "london-listings-2021-01-31-lesson-5-inference"

lab_5_model_path = tokyo_read_path + "tokyo-listings-2021-01-31-lab-5-model"
lab_5_inference_path = tokyo_read_path + "tokyo-listings-2021-01-31-lab-5-inference"

None

