from django.db import models

# Create your models here.
class Team(models.Model):
    """
    Represents a user in the system.

    Attributes:
        id (AutoField): The unique identifier for the user.
        name (CharField): The full name of the user.
        email (EmailField): The email address of the user.
        age (PositiveIntegerField): The age of the user.
        phone (CharField): The phone number of the user.
        access (CharField): The level of access granted to the user (e.g., 'admin', 'manager', 'user').
    """

    name = models.CharField(
        max_length=255,
        help_text="The full name of the Team member."
    )
    email = models.EmailField(
        unique=True,
        help_text="The email address of the Team member."
    )
    age = models.PositiveIntegerField(
        help_text="The age of the Team member."
    )
    phone = models.CharField(
        max_length=20,
        help_text="The phone number of the Team member."
    )
    access = models.CharField(
        max_length=20,
        choices=[('admin', 'Admin'), ('user', 'User'), ('manager', 'Manager')],
        default='user',
        help_text="The level of access granted to the user (e.g., 'admin', 'manager', 'user')."
    )

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return self.name




class Invoice(models.Model):
    """
    Represents an invoice.

    Attributes:
        id (AutoField): The unique identifier for the invoice.
        name (CharField): The full name associated with the invoice.
        email (EmailField): The email address associated with the invoice.
        cost (DecimalField): The cost of the invoice.
        phone (CharField): The phone number associated with the invoice.
        date (DateField): The date of the invoice.

    Methods:
        __str__(): Returns the name associated with the invoice.

    Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"
    """

    name = models.CharField(
        max_length=255,
        help_text="The full name associated with the invoice."
    )
    email = models.EmailField(
        help_text="The email address associated with the invoice."
    )
    cost = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text="The cost of the invoice."
    )
    phone = models.CharField(
        max_length=20,
        help_text="The phone number associated with the invoice."
    )
    date = models.DateField(
        help_text="The date of the invoice."
    )

    def __str__(self):
        """
        Returns the name associated with the invoice.

        Returns:
            str: The name associated with the invoice.
        """
        return self.name

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"



class CustomerContact(models.Model):
    """
    Represents a customer contact.

    Attributes:
        id (AutoField): The unique identifier for the customer contact.
        name (CharField): The full name of the customer contact.
        email (EmailField): The email address of the customer contact.
        age (PositiveIntegerField): The age of the customer contact.
        phone (CharField): The phone number of the customer contact.
        address (CharField): The address of the customer.
        city (CharField): The city of the customer.
        zipCode (CharField): The zipCode of the customer.
        registrarId (CharField): The registrarId of the customer.

    Methods:
        __str__(): Returns the name of the customer contact.

    Meta:
        verbose_name = "Customer Contact"
        verbose_name_plural = "Customer Contacts"
    """

    name = models.CharField(
        max_length=255,
        help_text="The full name of the customer contact."
    )
    email = models.EmailField(
        unique=True,
        help_text="The email address of the customer contact."
    )
    age = models.PositiveIntegerField(
        help_text="The age of the customer contact."
    )
    phone = models.CharField(
        max_length=20,
        help_text="The phone number of the customer contact."
    )
    address = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="The address of the customer."
    )
    city = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text="The city of the customer."
    )
    zipCode = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text="The zipCode of the customer."
    )
    registrarId = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text="The registrarId of the customer."
    )

    def __str__(self):
        """
        Returns the name of the customer contact.

        Returns:
            str: The name of the customer contact.
        """
        return self.name

    class Meta:
        verbose_name = "Customer Contact"
        verbose_name_plural = "Customer Contacts"



class Transactions(models.Model):
    """
    Represents a transaction.

    Attributes:
        txId (CharField): The unique identifier for the transaction.
        user (CharField): The full name of the user.
        cost (DecimalField): The cost on the product.
        date (DateField): The date of the invoice.

    Methods:
        __str__(): Returns the name associated with the Transaction.

    Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
    """

    txId = models.CharField(
        max_length=255,
        help_text="The ID associated with the invoice."
    )
    user = models.CharField(
        max_length=255,
        help_text="The email address associated with the invoice."
    )
    cost = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text="The cost of the product."
    )
    date = models.DateField(
        help_text="The date of the invoice."
    )

    def __str__(self):
        """
        Returns the name associated with the invoice.

        Returns:
            str: The name associated with the invoice.
        """
        return self.txId

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"



class BarData(models.Model):
    """
    Represents bar chart data.

    Attributes:
        country (CharField): The country of the data.
        Hotdog (IntegerField): The number of hot dogs sold.
        HotdogColor (CharField): The color of the hot dog bar.
        Burger (IntegerField): The number of burgers sold.
        BurgerColor (CharField): The color of the burger bar.
        Kebab (IntegerField): The number of kebabs sold.
        KebabColor (CharField): The color of the kebab bar.
        donut (IntegerField): The number of donuts sold.
        donutColor (CharField): The color of the donut bar.

    Methods:
        __str__(): Returns the name associated with the bar chart.

    Meta:
        verbose_name = "BarData"
        verbose_name_plural = "BarDatas"
    """

    country = models.CharField(
        max_length=255,
        help_text="The country of the data."
    )
    Hotdog = models.IntegerField(
        help_text="The number of hot dogs sold."
    )
    HotdogColor = models.CharField(
        max_length=255,
        help_text="The color of the hot dog bar."
    )
    Burger = models.IntegerField(
        help_text="The number of burgers sold."
    )
    BurgerColor = models.CharField(
        max_length=255,
        help_text="The color of the burger bar."
    )
    Kebab = models.IntegerField(
        help_text="The number of kebabs sold."
    )
    KebabColor = models.CharField(
        max_length=255,
        help_text="The color of the kebab bar."
    )
    donut = models.IntegerField(
        help_text="The number of donuts sold."
    )
    donutColor = models.CharField(
        max_length=255,
        help_text="The color of the donut bar."
    )

    def __str__(self):
        """
        Returns the name associated with the bar chart.

        Returns:
            str: The name associated with the bar chart.
        """
        return self.country

    class Meta:
        verbose_name = "BarData"
        verbose_name_plural = "BarDatas"



class PieData(models.Model):
    """
    Represents a transaction.

    Attributes:
        IDpie (CharField): The unique identifier for the piechart.
        label (CharField): The label associated with the piechart.
        value (IntegerField): The value associated with the piechart.
        colour (CharField): The colour associated with the piechart.

    Methods:
        __str__(): Returns the name associated with the Transaction.

    Meta:
        verbose_name = "PieData"
        verbose_name_plural = "PieDatas"
    """

    IDpie = models.CharField(
        max_length=255,
        help_text="The ID associated with the piechart."
    )
    label = models.CharField(
        max_length=255,
        help_text="The label associated with the piechart."
    )
    value = models.IntegerField(
        help_text="The value associated with the piechart."
    )
    colour = models.CharField(
        max_length=255,
        help_text="The colour associated with the piechart."
    )

    def __str__(self):
        """
        Returns the name associated with the piechart.

        Returns:
            str: The name associated with the piechart.
        """
        return self.IDpie
    
    class Meta:
        verbose_name = "PieData"
        verbose_name_plural = "PieDatas"



class LineData(models.Model):
    """
    Represents a transaction.

    Attributes:
        IDline (CharField): The unique identifier for the linechart.
        color (CharField): The colour associated with the linechart.
        data (JSONField()): The data associated with the linechart.

    Methods:
        __str__(): Returns the name associated with the LineData.

    Meta:
        verbose_name = "LineData"
        verbose_name_plural = "LineDatas"
    """

    IDline = models.CharField(
        max_length=255,
        help_text="The ID associated with the linechart."
    )
    color = models.CharField(
        max_length=255,
        help_text="The colour associated with the linechart."
    )
    data = models.JSONField(
        help_text="The data associated with the linechart."
    )
    def __str__(self):
        """
        Returns the name associated with the linechart.

        Returns:
            str: The name associated with the linechart.
        """
        return self.IDline
    
    class Meta:
        verbose_name = "LineData"
        verbose_name_plural = "LineDatas"
