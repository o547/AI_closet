from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import GarmentForm, CoordinateForm
from .models import garment, coordinate
from google import genai

# ----------keyを自分のapiキーに変更----------
cliant = genai.Client(api_key="key")
# ------------------------------------------

# Create your views here.


class IndexView(View):
    def get(self, request):
        return redirect("closet:garment_list")
        # return render(request,"closet/index.html")


class GarmentRegisterView(View):
    def get(self, request):
        form = GarmentForm()
        return render(request, "closet/garment_register.html", {"form": form})

    def post(self, request):
        form = GarmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("closet:garment_resistor")
        return render(request, "closet/garment_register.html", {"form": form})


class GarmentListView(View):
    def get(self, request):
        garments = garment.objects.all()
        return render(request, "closet/garment_list.html", {"garments": garments})


class GarmentDeleteView(View):
    def get(self, request, id):
        delete_garment = get_object_or_404(garment, id=id)
        delete_garment.delete()
        return redirect("closet:garment_list")


class CoordinateRegisterView(View):
    def get(self, request):
        form = CoordinateForm()
        garments = garment.objects.all()
        return render(
            request,
            "closet/coordinate_register.html",
            {"form": form, "garments": garments},
        )

    def post(self, request):
        form = CoordinateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("closet:coordinate_register")
        garments = garment.objects.all()
        return render(
            request,
            "closet/coordinate_register.html",
            {"form": form, "garments": garments},
        )


class CoordinateListView(View):
    def get(self, request):
        coordinates = coordinate.objects.all()
        return render(
            request, "closet/coordinate_list.html", {"coordinates": coordinates}
        )


class CoordinateDeleteView(View):
    def get(self, request, id):
        delete_coordinate = get_object_or_404(coordinate, id=id)
        delete_coordinate.delete()
        return redirect("closet:coordinate_list")


class AIEvaluationView(View):
    def get(self, request, id):
        evaluated_coordinate = coordinate.objects.get(id=id)
        prompt = "次の男性のコーディネートを100点満点で甘めに採点し、50文字程度のコメントをしてください。文字の装飾はしないでください。コーディネート："
        evaluated_coordinate_coordinate = ""
        if evaluated_coordinate.tops:
            evaluated_coordinate_coordinate = evaluated_coordinate_coordinate + str(
                evaluated_coordinate.tops
            )
        if evaluated_coordinate.bottoms:
            evaluated_coordinate_coordinate = (
                evaluated_coordinate_coordinate
                + " × "
                + str(evaluated_coordinate.bottoms)
            )
        if evaluated_coordinate.outer != "なし":
            evaluated_coordinate_coordinate = (
                evaluated_coordinate_coordinate
                + " × "
                + str(evaluated_coordinate.outer)
            )
        if evaluated_coordinate.inner != "なし":
            evaluated_coordinate_coordinate = (
                evaluated_coordinate_coordinate
                + " × "
                + str(evaluated_coordinate.inner)
            )
        if evaluated_coordinate.accessory != "なし":
            evaluated_coordinate_coordinate = (
                evaluated_coordinate_coordinate
                + " × "
                + str(evaluated_coordinate.accessory)
            )
        if evaluated_coordinate.additional1 != "なし":
            evaluated_coordinate_coordinate = (
                evaluated_coordinate_coordinate
                + " × "
                + str(evaluated_coordinate.additional1)
            )
        if evaluated_coordinate.additional2 != "なし":
            evaluated_coordinate_coordinate = (
                evaluated_coordinate_coordinate
                + " × "
                + str(evaluated_coordinate.additional2)
            )
        prompt = prompt + evaluated_coordinate_coordinate
        response = cliant.models.generate_content(
            model="gemini-2.0-flash-lite", contents=prompt
        )
        response = str(response.text)

        return render(
            request,
            "closet/ai_evaluation.html",
            {
                "response": response,
                "evaluated_coordinate_coordinate": evaluated_coordinate_coordinate,
            },
        )


class AICoordinateView(View):
    def get(self, request):
        garments = garment.objects.all()

        prompt = "次の衣服を自由に組み合わせて、男性向けコーディネートを一つ作ってください。文字の装飾はせずに「Tシャツ(白)×デニム(黒)」のように短文で返答してください。衣服リスト："
        for a_garment in garments:
            prompt = prompt + str(a_garment.name) + "(" + str(a_garment.color) + "),"
        response = cliant.models.generate_content(
            model="gemini-2.0-flash-lite", contents=prompt
        )
        response = str(response.text)
        return render(
            request,
            "closet/garment_list.html",
            {"garments": garments, "response": response},
        )


index = IndexView.as_view()
garment_resistor = GarmentRegisterView.as_view()
garment_list = GarmentListView.as_view()
garment_delete = GarmentDeleteView.as_view()
coordinate_register = CoordinateRegisterView.as_view()
coordinate_list = CoordinateListView.as_view()
coordinate_delete = CoordinateDeleteView.as_view()
ai_evaluation = AIEvaluationView.as_view()
ai_coordinate = AICoordinateView.as_view()
