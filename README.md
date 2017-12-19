# Knowman-Django-
Integrated Elastic Search for items

This is ElasticSearch in Django Project

1. Install the packages in requirements.txt
2. Install ElasticSearch on your computer
   1) ElasticSearch is Java application so to run this app, need to install JDK
   2) Download ElasticSearch and install
   3) run elasticsearch in terminal with following command
      (goto the parent folder of elasticsearch)
      ./elasticsearch_folder_name/bin/elasticsearch
      
      Please check if elasticsearch is running correctly by running ths command in terminal
      
        curl -XGET http://localhost:9200
        
      Then, it should display 
      {
        "name" : "6xIrzqq",
        "cluster_name" : "elasticsearch",
        "cluster_uuid" : "eUH9REKyQOy4RKPzkuRI1g",
        "version" : {
          "number" : "5.1.1",
          "build_hash" : "5395e21",
          "build_date" : "2016-12-06T12:36:15.409Z",
          "build_snapshot" : false,
          "lucene_version" : "6.3.0"
       },
       "tagline" : "You Know, for Search"
      
3. install elasticsearch-dsl
    pip install elasticsearch-dsl
4. Run django project.
