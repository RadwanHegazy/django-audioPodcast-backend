from django.test import TestCase
from .models import Stage, User
from uuid import uuid4
from django.urls import reverse
from rest_framework_simplejwt.tokens import AccessToken

class TestStageApp(TestCase) : 

    def setUp(self) -> None:
        self.get_all_stages_endpoint = reverse('get_all_stages')
        self.create_stage_endpoint = reverse('create_stage')

    def test_get_all_stages_endpoint(self) : 
        response = self.client.get(
            self.get_all_stages_endpoint
        )

        self.assertEqual(response.status_code, 200)

    def test_get_stage_by_uuid_faild(self) : 
        response = self.client.get(
            reverse('retrive_stage',args=[uuid4()])
        )
        self.assertNotEqual(response.status_code, 200)

    def test_get_stage_by_uuid_success(self) :
        u = User.objects.create(
            full_name='test',
            email='test@gmail.com'
        )
        stage = Stage.objects.create(
            owner=u
        ) 
        response = self.client.get(
            reverse('retrive_stage', args=[stage.id])
        )

        self.assertEqual(response.status_code, 200)
    
    def test_create_stage_faild(self) : 
        response = self.client.post(
            self.create_stage_endpoint
        )

        self.assertNotEqual(response.status_code, 200)

    def test_create_stage_faild(self) : 
        u = User.objects.create(
            full_name='test',
            email='test@gmail.com'
        )

        response = self.client.post(
            self.create_stage_endpoint,
            data={
                'title' : "test title"
            },
            headers={
                "Authorization" : f"Bearer {AccessToken.for_user(u)}"
            }
        )

        self.assertEqual(response.status_code, 201)