# Author: Bomi Oladimeji
# ID: 3164447
# Course: CMPT 200
# Assignment: Lab 3 - banking.py
# Collaborators: None
# Sources: Course lab materials

from queue import Queue
import random
from job_generator import * 
class Teller:
    """
    This class represents a bank teller that tracks service times, 
    availability, and customer interactions during the simulation.
    """
    def __init__(self,name = 'John'):
        """
        purpose: initialize a teller with a given name and default state attributes
        parameters: name: string representing the name/identifier of the teller
        throws: none
        pre: name must be provided or defaults to 'John'
        post: teller is initialized as available with zero service time
        returns: none
        """
        self.serving_customer = False
        self.name = name
        self.total_service_time = 0
        self.customer_remaining_service = 0 

    def get_name(self):
        """
        purpose: return the name of the teller
        parameters: none
        throws: none
        pre: Teller instance is initialized
        post: teller state remains unchanged
        returns: string representing the teller's name
        """
        return self.name

    def __str__(self):
        """
        purpose: return a formatted string containing teller information and total service time
        parameters: none
        throws: none
        pre: Teller instance is initialized
        post: teller state remains unchanged
        returns: string formatted as 'Teller: [name] Total service time:[time]'
        """
        return f'Teller: {self.name} Total service time:{self.total_service_time}'

    def service(self,serv_time):
        """
        purpose: simulate serving the current customer for a given time duration
        parameters: serv_time: integer representing the duration of the service cycle
        throws: none
        pre: Teller instance is initialized
        post: total service time and remaining customer service time are updated
        returns: none
        """
            
        if self.serving_customer == True:
            
            if serv_time < self.customer_remaining_service:
                        self.total_service_time += serv_time
                        self.customer_remaining_service -= serv_time
           
            else:
                 self.total_service_time += self.customer_remaining_service
                 self.customer_remaining_service -= self.customer_remaining_service
                 self.serving_customer = False

            
    def get_total_service_time(self):
        """
        purpose: return the total time spent by the teller serving customers
        parameters: none
        throws: none
        pre: Teller instance is initialized
        post: teller state remains unchanged
        returns: integer representing total service time
        """
        return self.total_service_time

    def accept(self, cust_time):
        """ 
        purpose: accept a new customer with a specified requested service time if available
        parameters: cust_time: integer representing the customer's requested service time
        throws: none
        pre: teller must not be currently serving another customer
        post: teller becomes occupied and tracks the customer's remaining time
        returns: none
        """
        if self.serving_customer == False:
            self.serving_customer = True
            self.cust_time = cust_time  
            self.customer_remaining_service = self.cust_time

    def make_available(self):
        """
        purpose: make the teller available to serve a new customer
        parameters: none
        throws: none
        pre: Teller instance is initialized
        post: serving_customer status is set to False
        returns: boolean status of serving_customer
        """
        self.serving_customer = False
        return self.serving_customer
    
    def is_available(self):
        """
        purpose: check if the teller is currently available to serve a customer
        parameters: none
        throws: none
        pre: Teller instance is initialized
        post: teller state remains unchanged
        returns: True if available, False otherwise
        """
        if self.serving_customer == False:
              return True
        else:
            return False


def banking_simulation():
    """
    purpose: run the bank simulation to manage tellers, customers, and commands
    parameters: none
    throws: none
    pre: Queue and Teller classes are implemented and available
    post: simulation runs and outputs statistics based on commands
    returns: none
    """
    queue = Queue()
    teller = Teller()
    create_customer_times(queue)
              
