class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class:VeiculoSerializer