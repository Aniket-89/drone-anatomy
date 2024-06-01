from django.db import models
from django.urls import reverse


class Drone(models.Model):
    name = models.CharField(max_length=225)
    model = models.CharField(max_length=225)
    featured_image = models.ImageField(
        upload_to="drones/",
        default="default.png",
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Drone"
        verbose_name_plural = "Drones"
        app_label = "drones"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    @classmethod
    def get_list_url(cls):
        """
        Returns the url to access the list of drones
        """
        return reverse("drone_anatomy.drones:drone-list")

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Drone.
        """
        return reverse(
            "drone_anatomy.drones:drone-detail",
            kwargs={
                "pk": self.pk,
            },
        )


class Feature(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    icon = models.ImageField(
        upload_to="drones/features",
        default="drones/features/default.png",
    )
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"

    def __str__(self):
        return self.name

    @property
    def drone_name(self):
        """
        Returns the name of the related drone
        """
        return self.drone.name

    @property
    def drone_url(self):
        """
        Returns the URL of the related drone without relying on get_absolute_url().
        """
        return reverse(
            "drone_anatomy.drones:drone-detail",
            kwargs={
                "pk": self.drone.id,
            },
        )


class Specification(models.Model):
    name = models.CharField(max_length=225)
    value = models.CharField(max_length=225)
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    icon = models.ImageField(
        upload_to="drones/specifications",
        default="drones/specifications/default.png",
    )

    class Meta:
        verbose_name = "Specification"
        verbose_name_plural = "Specifications"

    def __str__(self):
        return f"{self.name}: {self.value}"


class DroneImage(models.Model):
    photo = models.ImageField(upload_to="drones/")
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.caption
