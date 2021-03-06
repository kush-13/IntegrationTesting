import base64
from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    host = "http://host.docker.internal:80"
    @task
    def hello_world(self):
        # credentials for logging in          
        sample_string = "user:password"
        sample_string_bytes = sample_string.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64string = base64_bytes.decode("ascii")

        # exploring endpoints before auth
        self.client.get("/")
        self.client.get("/category.html")
        self.client.get("/basket.html")

        # cant access orders if not logged in
        with self.client.post("/orders", catch_response=True) as response:
            if response.status_code >= 400:
                response.success()

        # authoristion should be sucessfull with right details
        self.client.get("/login", headers={"Authorization":"Basic %s" % base64string})
        
        # accesing orders after logging in 
        self.client.post("/orders")
        
        # getting all the items in the catalogue 
        catalogue = self.client.get("/catalogue").json()

        # exploring items in catalogue
        # all the items url should be accesible i.e return 200 OK response
        for catalogue_item in catalogue:
            item_id = catalogue_item['id']
            
            # getting details of the items
            self.client.get("/detail.html?id={}".format(item_id))
            
            # posting items to the cart
            self.client.post("/cart", json={"id": item_id, "quantity": 1})

        # deleting the cart
        self.client.delete("/cart")
        
        
