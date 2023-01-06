from django.shortcuts import get_list_or_404, render, get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Pin, Board
from .serializers import PinSerializer, BoardSerializer


class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardDetail(APIView):
    
    def get_object(self, pk):
        return get_object_or_404(Board, id=pk)

    def get(self, request, pk, *args, **kwargs):
        board       = self.get_object(pk)
        serializer  = BoardSerializer(board)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        board       = self.get_object(pk)
        serializer  = BoardSerializer(board, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, *args, **kwargs):
        board   = self.get_object(pk)
        board.delete()
        return Response(status=204)


class BoardPinList(APIView):

    def get_queryset(self, board_id):
        queryset    = get_list_or_404(Pin, board__id=board_id)
        return queryset
    
    def get(self, request, board_id, *args, **kwargs):
        pins        = self.get_queryset(board_id)
        serializer  = PinSerializer(pins, many=True)
        return Response(serializer.data)
    
    def post(self, request, board_id, *args, **kwargs):
        request.data['board'] = board_id
        serializer = PinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        
    
class PinDetails(APIView):

    def get_object(self, board_id, pin_no):
        return get_object_or_404(Pin, board__id=board_id, pin_no=pin_no)

    def get(self, request, board_id, pin_no, *args, **kwargs):
        pin         = self.get_object(board_id, pin_no)
        serializer  = PinSerializer(pin)
        return Response(serializer.data)

    def put(self, request, board_id, pin_no, *args, **kwargs):
        pin         = self.get_object(board_id, pin_no)

        request.data['board'] = board_id
        request.data['pin_no'] = pin_no
        request.data['name'] = pin.name 

        serializer  = PinSerializer(pin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, board_id, pin_no, *args, **kwargs):
        pin = self.get_object(board_id, pin_no)
        pin.delete()
        return Response(status=200)


