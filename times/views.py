from django.shortcuts import render
from rest_framework.views import APIView, Request
from rest_framework.response import Response
from teams.models import Team
from django.forms.models import model_to_dict

# Create your views here.
class TeamViews(APIView):
    def post(self, req: Request):
        team_data = req.data
        new_team = Team.objects.create(**team_data)
        
        return Response(model_to_dict(new_team), 201)

    def get(self, req: Request):
        list_all_teams = Team.objects.all()
        teams_dict = []

        for team in list_all_teams:
            teams_dict.append(model_to_dict(team))

        return Response(teams_dict)


class TeamViewId(APIView):
    def get(self, req: Request, team_id: int):
        try:
            find_team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

        team_dict = model_to_dict(find_team)

        return Response(team_dict)

    def patch(self, req: Request, team_id: int):
        try:
            find_team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

        for key, value in req.data.items():
            setattr(find_team, key, value)
        
        find_team.save()
        team_dict = model_to_dict(find_team)

        return Response(team_dict, 200)

    def delete(self, req: Request, team_id: int):
        try:
            find_team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

        find_team.delete()

        return Response(status=204)