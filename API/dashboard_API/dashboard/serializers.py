from rest_framework import serializers
from .models import Team, CustomerContact, Invoice, Transactions, BarData, PieData, LineData

class TeamSerializer(serializers.ModelSerializer):
    """
    A generic serializer that can be used for multiple models.

    Attributes:
        model (Model): The model class to be serialized.

    Meta:
        model (Model): The model class to be set dynamically.
        fields (str or tuple): The fields to include in the serialized representation.

    Example Usage:
        To use this serializer, set the `model` attribute before serializing data.
        serializer = GenericModelSerializer(model=YourModel, fields='__all__')
    """
    class Meta:
        model = Team
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    """
    A generic serializer that can be used for multiple models.

    Attributes:
        model (Model): The model class to be serialized.

    Meta:
        model (Model): The model class to be set dynamically.
        fields (str or tuple): The fields to include in the serialized representation.

    Example Usage:
        To use this serializer, set the `model` attribute before serializing data.
        serializer = GenericModelSerializer(model=YourModel, fields='__all__')
    """
    class Meta:
        model = CustomerContact
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    """
    A generic serializer that can be used for multiple models.

    Attributes:
        model (Model): The model class to be serialized.

    Meta:
        model (Model): The model class to be set dynamically.
        fields (str or tuple): The fields to include in the serialized representation.

    Example Usage:
        To use this serializer, set the `model` attribute before serializing data.
        serializer = GenericModelSerializer(model=YourModel, fields='__all__')
    """
    class Meta:
        model = Invoice
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    """
    A generic serializer that can be used for multiple models.

    Attributes:
        model (Model): The model class to be serialized.

    Meta:
        model (Model): The model class to be set dynamically.
        fields (str or tuple): The fields to include in the serialized representation.

    Example Usage:
        To use this serializer, set the `model` attribute before serializing data.
        serializer = GenericModelSerializer(model=YourModel, fields='__all__')
    """
    class Meta:
        model = Transactions
        fields = '__all__'

class BarDataSerializer(serializers.ModelSerializer):
    """
    A generic serializer that can be used for multiple models.

    Attributes:
        model (Model): The model class to be serialized.

    Meta:
        model (Model): The model class to be set dynamically.
        fields (str or tuple): The fields to include in the serialized representation.

    Example Usage:
        To use this serializer, set the `model` attribute before serializing data.
        serializer = GenericModelSerializer(model=YourModel, fields='__all__')
    """
    class Meta:
        model = BarData
        fields = '__all__'

class PieDataSerializer(serializers.ModelSerializer):
    """
    A generic serializer that can be used for multiple models.

    Attributes:
        model (Model): The model class to be serialized.

    Meta:
        model (Model): The model class to be set dynamically.
        fields (str or tuple): The fields to include in the serialized representation.

    Example Usage:
        To use this serializer, set the `model` attribute before serializing data.
        serializer = GenericModelSerializer(model=YourModel, fields='__all__')
    """
    class Meta:
        model = PieData
        fields = '__all__'

class LineDataSerializer(serializers.ModelSerializer):
    """
    A generic serializer that can be used for multiple models.

    Attributes:
        model (Model): The model class to be serialized.
    
    Meta:
        model (Model): The model class to be set dynamically.
        fields (str or tuple): The fields to include in the serialized representation.

    Example Usage:
        To use this serializer, set the `model` attribute before serializing data.
        serializer = GenericModelSerializer(model=YourModel, fields='__all__')
    """
    class Meta:
        model = LineData
        fields = '__all__'
