"""
Views for the fhir_api Opal Plugin
"""
import pprint
from django.views.generic import TemplateView
from opal.models import Patient, UserProfile

from fhirclient import client
import fhirclient.models.patient as p
import fhirclient.models.fhirsearch as s
import fhirclient.models.medicationrequest as meds
import fhirclient.models.medication as mednames
import fhirclient.models as fhirmodels


class FhirViewSet(TemplateView):

    template_name = "modals/test_fhir.html"

    def get_context_data(self, patient_id, episode_id, hospital_number):
        #pprint.pprint(dir(request.request.user))
        # user_profile = UserProfile.objects.get(pk=request.request.user.pk)
        # pprint.pprint(dir(user_profile))
        settings = {"app_id": "my_web_app", "api_base": "https://r3.smarthealthit.org"}

        smart = client.FHIRClient(settings=settings)

        patient = s.FHIRSearch(p.Patient, {"_id": "smart-767980"}).perform(smart.server)
        json_pt = patient.as_json()

        # pprint.pprint(json_pt["entry"][0]["resource"])
        patient = json_pt["entry"][0]["resource"]
        patient_object = {
            "birthdate": patient["birthDate"],
            "first_name": patient["name"][0]["given"][0],
            "surname": patient["name"][0]["family"],
        }

        medications = meds.MedicationRequest.where(
            struct={"subject": "smart-767980", "status": "active"}
        ).perform_resources(smart.server)
        medlist = []
        for medication in medications:
            medref = medication.as_json()
            # pprint.pprint(medref)
            med_object = {
                "name": medref["medicationCodeableConcept"]["text"],
                "dosage": medref["dosageInstruction"][0]["text"],
            }
            medlist.append(med_object)

        context = {"patient": patient_object, "medication": medlist}
        Patient().bulk_update(
            {
                "demographics": [{"hospital_number": hospital_number}],
                "drug_history": [{"Medications": medlist}],
            },
            #request.request.user.username,
            self.request.user,
            episode=episode_id,
        )

        return context