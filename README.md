# **Intrigue Splunk App**

This is the official Intrigue.io Splunk App

The purpose of the Intrigue Splunk App is to collect information from the [Intrigue APIs](https://help.intrigue.io/reference/authenticating-to-intrigueio-apis) on an interval basis (specified by the user).

## **Installation instruction**

### **Requirements**

* Intrigue membership

* Splunk Enterprise 8.x

* Python 3.x (For best results)

### **Import Steps**

1. Download the latest Intrigue-x.x.x.spl.

1. Log into splunk.

1. Navigate to "Manage Apps".

1. Press "Install app from file".

1. Select Intrigue-x.x.x.spl file.

## **Usage instruction**

### **How to setup an input for data collection**

1. Log into splunk.

1. Select the Intrigue App.

1. Press "Create New Input"

    * Name - User defined name for your collection.
    * Interval - Interval in seconds on which the input will operate (min 6h, max 12h)
    * Index - default(main) for more information on indexes consult [Splunk documentation](https://docs.splunk.com/Documentation/Splunk/8.1.0/Indexer/Aboutmanagingindexes)
    * Collection name - This is the collection you want to get information from. This infromation can be found on your Intrigue account under ["My Collections"](https://app.intrigue.io/user/collections). The value to ve used here will be next to the collection name under "()" eg: (xxx_xxxxx)
    * Item Type - [Collection Type](https://help.intrigue.io/reference/collection-export-by-date#valid-item-types).
    * Access Key - This information can be access through ["My Profile"](https://app.intrigue.io/user/profile) on intrigue under "API Access". If you don't have one you can press "Generate New API Key" to create one.
    * Secret Key - This information is obtained when you press "Generate New API Key" under your ["My Profile"](https://app.intrigue.io/user/profile) on intrigue.

### **How to vizualise collected data**

1. Log into splunk.

1. Select the Intrigue App.

1. Press "Search" on the top bar.

1. Press "Data Summary".

    * Select either by "Host", "Sources" or "SourceType", whichever is relevant for the use case.
1. The data should now appear in a queryable format.
